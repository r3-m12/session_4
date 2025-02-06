import time
ma_variable_globale = "Variable globale"
def fonction(ma_variable_argument):
    ma_variable_locale = "Variable locale"
    for var in [ma_variable_globale, ma_variable_argument, ma_variable_locale]:
        print(var)
        time.sleep(0.5)  
fonction("Variable argument")