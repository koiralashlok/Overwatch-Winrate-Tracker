import pandas as pd

global PATH
global WINRATE_DF


def readDf(winrateDf: pd.DataFrame):
    global WINRATE_DF

    # df provided -> called from code
    if not winrateDf is None:
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
#   1. When called from code, winrateDf must be provided
#       winrate data is not read, instead given df is used
#       ETL result is returned not written to any path
#   2. When called from CLI, winrate df is null
#       winrate data is read from PATH
#       ETL result is written
def main(winrateDf: pd.DataFrame = None):
    # TODO make this run standalone too (if etl.main() is run)
    global WINRATE_DF
    global PATH

    # TODO dynamic path
    PATH = '../Winrate Tracker/db/winrate.csv'
    
    # Read the CSV file
    readDf(winrateDf)

    # Perform transformations
    add_winrate_column()

    # Save the updated DataFrame
    if not winrateDf is None: 
        return WINRATE_DF
    else:
        saveDf()


if __name__ == '__main__':
    main()