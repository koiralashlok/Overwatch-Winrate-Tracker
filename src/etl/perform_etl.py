import pandas as pd

global WINRATE_DF

def readDf(winrateDf: pd.DataFrame):
    global WINRATE_DF

    if not winrateDf is None:
        print("in if")
        WINRATE_DF = winrateDf
        return
    else: # else should be unnecessary
        print("in else")
        # Read the CSV file
        WINRATE_DF = pd.read_csv('../../db./winrate.csv')
        print(WINRATE_DF)


def add_winrate_column():
    global WINRATE_DF
    print("Adding winrate column...")
    WINRATE_DF['winrate'] = WINRATE_DF['num_of_wins'] * 100 / (WINRATE_DF['num_of_wins'] + WINRATE_DF['num_of_losses'])


def saveDf():
    global WINRATE_DF
    print("Saving Changes...")
    WINRATE_DF.to_csv('../../db./winrate.csv', index=False)


def main(winrateDf: pd.DataFrame = None):
    # TODO make this run standalone too (if etl.main() is run)
    global WINRATE_DF
    
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