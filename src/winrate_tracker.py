import pandas as pd
import etl.perform_etl as etl

WIN = 'win'
LOSS = 'loss'

def updateWinrate(map_name, result):
    try:
        # TODO path name needs to be dynamic somehow
        # TODO avoid reading the df over and over (maybe use a global variable?)
        # Load existing winrate data
        winrate_data = pd.read_csv('db./winrate.csv')
    except FileNotFoundError:
        winrate_data = pd.DataFrame(columns=['map', 'wins', 'losses'])

    # Update winrate data
    if not winrate_data.empty:
        map_row = winrate_data[winrate_data['map'] == map_name]
        if not map_row.empty:
            index = map_row.index[0]
            if result.lower() == WIN:
                winrate_data.at[index, 'wins'] += 1
            elif result.lower() == LOSS:
                winrate_data.at[index, 'losses'] += 1
        else:
            if result.lower() == WIN:
                winrate_data = pd.concat([winrate_data, pd.DataFrame({'map': [map_name], 'wins': [1], 'losses': [0]})])
            elif result.lower() == LOSS:
                winrate_data = pd.concat([winrate_data, pd.DataFrame({'map': [map_name], 'wins': [0], 'losses': [1]})])
    else:
        if result.lower() == WIN:
            winrate_data = pd.DataFrame({'map': [map_name], 'wins': [1], 'losses': [0]})
        elif result.lower() == LOSS:
            winrate_data = pd.DataFrame({'map': [map_name], 'wins': [0], 'losses': [1]})

    # TODO - Remove this line, instead calcualte winrate inside the update function
    # Perform ETL
    winrate_data = etl.main(winrate_data)
    # Write updated winrate data to CSV
    winrate_data.to_csv('db./winrate.csv', index=False)

def viewWinrate():
    try:
        # Load and print winrate data
        winrate_data = pd.read_csv('db./winrate.csv')
        print(winrate_data.to_string(index=False))
    except FileNotFoundError:
        print("Winrate data not found.")

def viewWinrateByMap(map_name):
    try:
        # Load and print winrate data
        winrate_data = pd.read_csv('db./winrate.csv')
        map_row = winrate_data[winrate_data['map'] == map_name]
        if not map_row.empty:
            print(map_row.to_string(index=False))
        else:
            print("Map not found.")
    except FileNotFoundError:
        print("Winrate data not found.")

def viewAggregate():
    try:
        # Load and print winrate data
        winrate_data = pd.read_csv('db./winrate.csv')
        print("Aggregate winrate: {:.2f}%".format((winrate_data['wins'].sum() * 100) / (winrate_data['wins'].sum() + winrate_data['losses'].sum())))
    except FileNotFoundError:
        print("Winrate data not found.")

def printMenu():
    print("Enter map name and result (win/loss), separated by space.")
    print("Type 'view' to see the current winrate data.")
    print("Type 'exit' to quit.")

def main():
    print("Welcome to Winrate Tracker!")
    printMenu()

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
