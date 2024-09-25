import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt
from reliability.Distributions import Weibull_Distribution
def jls_extract_def():
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
    return selected


def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print("************************************************")
	print("*****  Hello - Hessam Hosseini  ******")
	print("************************************************")
	selected = jls_extract_def()
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

def pandasopenai():
    #from pandasai import SmartDataframe
    df = pd.DataFrame({
    "country": [
        "United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [
        19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064
    ],
    })
    # moghayse mafhoom jomlaat
    tags="AFTER T/S FOUND DUC TEMP SENSOR FAULTY , SO REPLACED WITH S/P IAW AMM 21-60-21 P 201 CHECK FOUND OK."

    multi = "pip install aspose-words"
    tasks={"defect1": tags, "defect2": multi}

    
    actions = ["AFTER T/S FOUND DUC TEMP SENSOR FAULTY , SO REPLACED WITH S/P IAW AMM 21-60-21 P 201 CHECK FOUND OK.","PACK VLV #2 REPLACED WITH S/P IAW 21-10-11 PB 401."]
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    tfid=TfidfVectorizer()
    tfid_matrix=tfid.fit_transform(tasks)
    similariy=cosine_similarity(tfid_matrix[0],tfid_matrix[1])
    print(similariy)
    tfidf = TfidfVectorizer(analyzer='char_wb', ngram_range=(1, 2))
    text = ['sachin is a good player .', 'he is a good man .']
    X = tfidf.fit_transform(actions)
    print(tfidf.get_feature_names_out())

def weibull_predict():
    from predictr import Analysis
    # Data from testing
    # Failures and suspensions are lists containing the values
    
    suspensions = [1.62876357, 1.62876357, 1.62876357, 1.62876357]
    # Weibull Analysis
    #x = Analysis(df=failures, ds=suspensions, show=True)
    
    #x.mrr()
    #x.mle()
    df = pd.DataFrame({
    "TTF": [ 
        180, 450, 740, 1040, 1360, 1700, 2070, 2460, 2890, 3380, 3870, 4430, 5070 ,5790 ,6630, 7530, 8880, 10520, 12920, 17540

    ]
    })
    print(df.head)
    #print(f"MRR: beta={x.beta:2f}, eta={x.eta:2f}\nMLE: beta={y.beta:2f}, eta={y.eta:2f}\n")
    
def new_analyze():
        # code
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy.stats as ss
    import numpy as np
    import seaborn as sns
    import weibull

    # generate standard weibull distribution of different Shape parameter
    gamma_1 = np.random.weibull(a=1,size=1000)
    gamma_half = np.random.weibull(a=0.5,size=1000)
    gamma_5 = np.random.weibull(a=5,size=1000)
    gamma_10 = np.random.weibull(a=10,size=1000)

    # plot different Weibull distribution
    sns.set_style('darkgrid')
    fig, ax = plt.subplots(2,2)
    sns.histplot(gamma_1,kde=True,ax= ax[0,0] )
    ax[0,0].set_title('Gamma = 1 ')
    sns.histplot(gamma_half,kde=True, ax= ax[0,1], legend='Y=0.5')
    ax[0,1].set_ylim([0,200])
    ax[0,1].set_title('Gamma = 0.5 ')
    sns.histplot(gamma_5,kde=True, ax= ax[1,0], legend='Y=5')
    ax[1,0].set_title('Gamma = 5 ')
    sns.histplot(gamma_10,kde=True, ax= ax[1,1], legend='Y=10')
    ax[1,1].set_title('Gamma = 10 ')
    plt.show()

    # load dataset
    specimen_strength = pd.DataFrame({
    
    "index": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    "TTF": [ 
        180, 450, 740, 1040, 1360, 1700, 2070, 2460, 2890, 3380, 3870, 4430, 5070 ,5790 ,6630, 7530, 8880, 10520, 12920, 17540

    ]
    
    })
    #specimen_strength = pd.read_csv('weibull.csv', header=None)
    specimen_strength.head()

    # perform weibull analysis
    analysis=weibull.Analysis(specimen_strength[0])

    # Here, we can fit using two method, mle (maximum likelihood)
    # and lr (linear regression). Generally mle is better fit
    analysis.fit(method='lr')

    # print shape parameter (Beta) and scale parameter (eta)
    print(f'shape Parameter: {analysis.beta: .02f}')
    print(f'Scale Parameter: {analysis.eta: .02f}')

    # print values of different parameters confidence interval
    analysis.stats

    # generate Weibull probplot
    analysis.probplot()

def analysis():
    from reliability.Probability_plotting import plotting_positions
    from reliability.Distributions import Weibull_Distribution
    from reliability.Probability_plotting import plot_points
    import matplotlib.pyplot as plt
    from reliability.Convert_data import xlsx_to_FR
    data_from_excel = xlsx_to_FR(path=r'FR.xlsx')
    failures = [150,560,800,1720,5230,6890]
    right_censored = [340,1130,2470,4210]
    x,y=plotting_positions(failures=data_from_excel.failures,right_censored=data_from_excel.right_censored)

    print('x =',x)
    print('y =',y)
    dist = Weibull_Distribution(alpha=100,beta=2)
    data = dist.random_samples(1000,seed=1)

    functions = ['PDF','CDF','SF','HF','CHF']
    i = 0
    for function in functions:
        plt.subplot(151+i)
        if function == 'PDF':
            dist.PDF()
        elif function == 'CDF':
            dist.CDF()
        elif function == 'SF':
            dist.SF()
        elif function == 'HF':
            dist.HF()
        elif function == 'CHF':
            dist.CHF()
        plot_points(failures=data_from_excel.failures,func=function)
        plt.title(function)
        i+=1
    plt.gcf().set_size_inches(12,4)
    plt.tight_layout()
    plt.show()
 


display_menu()