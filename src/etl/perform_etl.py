import pandas as pd
import sys

global PATH
global WINRATE_DF
global CALLED_FROM_CLI

def readDf(winrateDf: pd.DataFrame):
    global WINRATE_DF

    # df provided -> called from code
    if not CALLED_FROM_CLI:
        WINRATE_DF = winrateDf
        return
    # called from cli
    else:
        # Read the CSV file
        WINRATE_DF = pd.read_csv(PATH)


def add_winrate_column():
    global WINRATE_DF

    print("Adding winrate column...")
    WINRATE_DF['winrate'] = WINRATE_DF['wins'] * 100 / (WINRATE_DF['wins'] + WINRATE_DF['losses'])


def saveDf():
    global WINRATE_DF

    print("Saving Changes...")
    WINRATE_DF.to_csv(PATH, index=False)


# Two ways this function should be called
#   1. When called from code, winrateDf must be provided not path
#       winrate data is not read, instead given df is used
#       ETL result is returned not written to any path
#   2. When called from CLI, path is provided not winrateDf
#       winrate data is read from path
#       ETL result is written
def main(winrateDf: pd.DataFrame = None):
    global WINRATE_DF
    global PATH
    global CALLED_FROM_CLI

    CALLED_FROM_CLI = winrateDf is None

    try:
        # try getting first cli argument
        pathFromCli = sys.argv[1]
    except:
        # no cli argument and no df provided
        if CALLED_FROM_CLI:
            raise ValueError("If called from CLI, please provide `path` as an argument else provide `winrateDf`")
    # At this point, either path is not None OR winrateDf is not None

    PATH = '../Winrate Tracker/db/winrate.csv' if not CALLED_FROM_CLI else pathFromCli
    
    # Read the CSV file
    readDf(winrateDf)

    # Perform transformations
    add_winrate_column()

    # Save the updated DataFrame
    if not CALLED_FROM_CLI: 
        return WINRATE_DF
    else:
        saveDf()


if __name__ == '__main__':
    main()