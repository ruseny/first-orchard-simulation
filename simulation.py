"""
The module to simulate the game First Orchard and report the results.
"""

from game import FirstOrchard
from pandas import DataFrame # to save the result in a tidy format
from datetime import datetime # to timestamp the results

def simulate_game(num_simulations: int = 1000, mode: str = "smart", verbose: bool = False):
    game = FirstOrchard(mode=mode, verbose=verbose)
    
    # save results in a dictionary of lists, with keys same as the export_summary() method
    results = {
        "num_rounds" : [],
        "result" : [], 
        "rem_blue" : [],
        "rem_green" : [],
        "rem_red" : [],
        "rem_yellow" : [],
        "rem_crow_tiles" : []
        }
    
    for _ in range(num_simulations):
        game.play_game()
        for stat in game.export_summary():
            results[stat].append(game.export_summary()[stat]) # add each result to the corresponding list
        game.reset_game()
        
    return DataFrame(results)

# collect parameters as user input: number of simulations, game mode, verbose, save file
def sim_num_input():
    simulation_num = input("Number of simulations: ")
    try:
        simulation_num = int(simulation_num)
    except ValueError:
        print("Your input should be an integer.")
        prompt_again = input("Do you want to try again? [yes or no]: ")
        if prompt_again == "yes":
            return sim_num_input()
        else:
            print("The default number 1000 will be used.")
            return 1000
    return simulation_num

def mode_input():
    mode = input("Game mode ['smart' or 'random']: ")
    if mode not in ["smart", "random"]:
        print("Your input should be either 'smart' or 'random'.")
        prompt_again = input("Do you want to try again? [yes or no]: ")
        if prompt_again == "yes":
            return mode_input()
        else:
            print("The default mode 'smart' will be used.")
            return "smart"
    return mode

def verbose_input():
    verbose_str = input("Do you want to print every round? ['yes' or 'no]: ")
    if verbose_str not in ["yes", "no"]: 
        print("Your input should be either 'yes' or 'no'.")
        prompt_again = input("Do you want to try again? [yes or no]: ")
        if prompt_again == "yes":
            return verbose_input()
        else:
            print("By default, the rounds will not be printed.")
            return False
    if verbose_str == "yes":
        return True
    else:
        return False

def save_file_input():
    save_file = input("Save results as csv? [yes or no]: ")
    if save_file not in ["yes", "no"]:
        print("Your input should be either 'yes' or 'no'.")
        prompt_again = input("Do you want to try again? [yes or no]: ")
        if prompt_again == "yes":
            return save_file_input()
        else:
            print("By default, the results will not be saved as csv.")
            return "no"
    return save_file


if __name__ == "__main__":
    
    # user-defined parameters:
    simulation_num = sim_num_input()
    mode = mode_input()
    verbose = verbose_input()
    save_file = save_file_input()
    
    # running simulations
    df_results = simulate_game(num_simulations=int(simulation_num), mode=mode, verbose=verbose)

    # saving results to a file if requested
    if save_file == "yes":
        df_results.to_csv(f"simulation_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")

    # printing summary statistics
    print(df_results.value_counts("result", normalize = True))