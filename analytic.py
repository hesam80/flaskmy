import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt
from reliability.Distributions import Weibull_Distribution
def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print("************************************************")
	print("*****  Hello - Hessam Hosseini  ******")
	print("************************************************")
	selected = input(f"""WHICH ONE? (1-8)
	1) RUN pandas_practce
	2) RUN op_one
	3) RUN task to do
	4) RUN tahlil_defect
	5) RUN tahlil_defect_op1
	6) RUN str practice
	7) RUN weibull_predict
	8) Run new_analyze
	9) Run sendsms BTC pass
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		tahlil()
	elif selected=="2":
		#insert_to_excel()
		pass
	elif selected=="3":
		import_from_excel()
def tahlil():
    dist = Weibull_Distribution(alpha=50, beta=1)
    sf = dist.SF(20)
    print('The value of the SF at 20 is', round(sf * 100, 2), '%') #converting the decimal answer

def import_from_excel():
    from reliability.Convert_data import xlsx_to_FR
    from reliability.Fitters import Fit_Weibull_2P
    from reliability.Other_functions import crosshairs
    import matplotlib.pyplot as plt
    data = xlsx_to_FR(path=r'FR.xlsx')
    Fit_Weibull_2P(failures=data.failures, quantiles=True, CI=0.8, show_probability_plot=False)
    print('----------------------------------------------------------')
    # repeat the process but using specified quantiles.
    output = Fit_Weibull_2P(failures=data.failures, quantiles=[0.05, 0.5, 0.95], CI=0.8)
    # these points have been manually annotated on the plot using crosshairs
    crosshairs()
    plt.show()

    # the values from the quantiles dataframe can be extracted using pandas:
    lower_estimates = output.quantiles['Lower Estimate'].values
    print('Lower estimates:', lower_estimates)

    #alternatively, the bounds can be extracted from the distribution object
    lower,point,upper = output.distribution.CDF(CI_y=[0.05, 0.5, 0.95], CI=0.8)
    print('Upper estimates:', upper)
    #print(data.failures)
    #print(data.right_censored)
    #data.print()
    


display_menu()