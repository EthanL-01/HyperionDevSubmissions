:: Changes current directory to hyp_example
cd hyp_example
:: Creates a new directory called if_folder if new_folder exists in hyp_example
if exist new_folder mkdir if_folder
:: Creates a new directory called hyperionDev if new_folder exists 
:: in hyp_example, or a directory called new-projects if it does not
if exist if_folder (mkdir hyperionDev) else (mkdir new-projects)
