from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from winrate_tracker_app.src import winrate_tracker as wt
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import datetime
import zlib
import pickle
import json
from pathlib import Path

# TODO use rel path!!
DB_PATH = Path(__file__).resolve().parent.parent / 'winrate.csv'

# TODO can these be project wide global variables like env vars or something maybe in secrets idk
CACHE_TIMEOUT_DURATION = 3600 # seconds
FAILED_RESPONSE = {
            "message": "No id provided!",
            "payload_type": f"{type(None)}",
            "payload": None
        }
WINRATE_CACHE_PREFIX = 'winrate_data_'

def _compress_and_cache(df: pd.DataFrame, cache_key: str):
    cache.set(cache_key, zlib.compress(pickle.dumps(df)), timeout=CACHE_TIMEOUT_DURATION)

def _decompress_cached_data(compressed_df: bytes) -> pd.DataFrame: 
    return pickle.loads(zlib.decompress(compressed_df))

@api_view(['GET'])
def ping_frontend(request, id=None):
    
    message=f"Your id is {id}"
    return JsonResponse({
        "ts": f"{datetime.datetime.now()}",
        "message": message
    })

@api_view(['GET'])
def get_winrate_data_by_id(request, id):
    # TODO could have id and fetch diff cache/db per id maybe??
    #   or could save everything in same db (id, map, win, loss) and parse into query while fetching
    #   SQL would look something like f"select * from winrate_db where id = {id}"
    # TODO do not cache df if too big!
    
    # Initialize response
    response = FAILED_RESPONSE

    # TODO I think this is unreachable
    if not id:
        return JsonResponse(response)

    winrate_cache_key = WINRATE_CACHE_PREFIX + id
    # compressed_winrate_data = cache.get(winrate_cache_key)

    winrate_data = (pd.read_csv(DB_PATH)).to_dict()

    # if not compressed_winrate_data:
    #     winrate_data = pd.read_csv(DB_PATH)
    #     # TODO pull out data for "id" here, cahce only that!
    #     _compress_and_cache(winrate_data, winrate_cache_key)
    # else:
    #     winrate_data = _decompress_cached_data(compressed_winrate_data)
    
    # Update response to send   
    response["message"] = f"winrate data for id={id}"
    response["payload_type"] = f"{type(winrate_data)}"
    response["payload"] = winrate_data # TODO can we send df or does it need to be a dict

    return JsonResponse(response)

@api_view(['POST']) # TODO is this the correct type of req
def update_db(request, id):
    # TODO: recieve update from fe (hopefully just the updated row now the whole df)
    updated_winrate_data = pd.DataFrame()
    winrate_cache_key = WINRATE_CACHE_PREFIX + id
    # TODO join the updated row with the whole df and write
    # _compress_and_cache(updated_winrate_data, winrate_cache_key)
    pass

def index(request):
    return HttpResponse("Hello, world. You're at the TRACKER PAGE.")

def someView(request):
    result = wt.test("my message")
    return HttpResponse(f"{result}")

def showTrackerOptions(request):
    # TODO replace with sqlite
    path = '../winrate.csv'
    # Just as a fail-safe
    try:
        wt.readWinrateData(path)
    # Bubble up other exceptions (ex: permissions)
    except FileNotFoundError:
        print("No winrate data found!\nExiting...")
        return

    while True:
        user_input = input("Enter input: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        else:
            try:
                map_name, result = user_input.split(sep=' ')

                if map_name.lower() == 'view':
                    if result.lower() == 'aggregate':
                        wt.viewAggregate()
                    else:
                        wt.viewWinrateByMap(result)
                else:
                    wt.updateWinrate(map_name, result)
                    print("Winrate updated successfully!")
            except ValueError:
                if user_input.lower() == 'view':
                    wt.viewWinrate()
                else:
                    print("Invalid input format!")
                    wt.printMenu()