import pandas as pd
import etl.perform_etl as etl

WIN = 'win'
LOSS = 'loss'

global WINRATE_DF
global PATH

def readWinrateData():
    global WINRATE_DF

    # try:
        # Load existing winrate data
    WINRATE_DF = pd.read_csv(PATH)
    # Bubble up other exceptions (ex: permissions)
    # except FileNotFoundError:
    #     # Just a fail-safe (batch file should make the csv)
    #     WINRATE_DF = pd.DataFrame(columns=['map', 'wins', 'losses'])


def saveWinrateData(winrate_df):
    global WINRATE_DF

    # Update df and csv
    WINRATE_DF = winrate_df
    WINRATE_DF.to_csv(PATH, index=False)


def updateWinrate(map_name, result):
    global WINRATE_DF

    winrate_data = WINRATE_DF
    map_row = winrate_data[winrate_data['map'] == map_name]
    
    # Map already exists in db simply update stats
    if not map_row.empty:
        winrate_data = winrate_data.drop(map_row.index)
        # TODO the updates (lines 41 and 43) result in SettingWithCopyWarning
        if result.lower() == WIN:
            map_row['wins'] += 1
        elif result.lower() == LOSS:
            map_row['losses'] += 1
    # Provided map doesn't exist in db yet
    else:
        if result.lower() == WIN:
            map_row = pd.DataFrame({'map': [map_name], 'wins': [1], 'losses': [0]})
        elif result.lower() == LOSS:
            map_row = pd.DataFrame({'map': [map_name], 'wins': [0], 'losses': [1]})
        
    # Perform Transform
    map_row = etl.main(map_row)
    winrate_data = pd.concat([winrate_data, map_row], ignore_index=True)

    # Perform Load
    saveWinrateData(winrate_data)


def viewWinrate():
    print(WINRATE_DF.to_string(index=False))


def viewWinrateByMap(map_name):
    map_row = WINRATE_DF[WINRATE_DF['map'] == map_name]
    if not map_row.empty:
        print(map_row.to_string(index=False))
    else:
        print(f"No data found for map {map_name}")


def viewAggregate():
    totalWins = WINRATE_DF['wins'].sum()
    totalLosses = WINRATE_DF['losses'].sum()
    totalPlayed = totalWins + totalLosses

    print("Games played: {0}".format(totalPlayed))
    print("Wins: {0}".format(totalWins))
    print("Losses: {0}".format(totalLosses))
    print("Overall winrate: {:.2f}%".format((WINRATE_DF['wins'].sum() * 100) / (WINRATE_DF['wins'].sum() + WINRATE_DF['losses'].sum())))


def printMenu():
    print("Enter map name and result (win/loss), separated by space.")
    print("Type 'view' to see the current winrate data.")
    print("Type 'view mapname' to see stats for a particular map.")
    print("Type 'view aggregate' to see the aggregate winrate.")
    print("Type 'exit' to quit.")


def main():
    global PATH, WINRATE_DF
    print("Welcome to Winrate Tracker!")
    printMenu()

    # TODO ensure try except block works
    PATH = 'db/winrate.csv'
    try:
        readWinrateData()
    except FileNotFoundError:
        try:
            PATH = '../db/winrate.csv'
            readWinrateData()
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
                        viewAggregate()
                    else:
                        viewWinrateByMap(result)
                else:
                    updateWinrate(map_name, result)
                    print("Winrate updated successfully!")
            except ValueError:
                if user_input.lower() == 'view':
                    viewWinrate()
                else:
                    print("Invalid input format!")
                    printMenu()


if __name__ == "__main__":
    main()
