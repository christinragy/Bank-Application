from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'Application'


loan_amount =5000 
Interest_Rate =15
fees = 3
loan_period = 0
total_amount =0
account_amount= 12000


def check_balance(account_amount, loan_amount, fees):
	if(account_amount >= (loan_amount+fees)):
		loan_status = "funded"
	else:
		loan_status= "rejected"
		
def submit_loan(account_amount, loan_amount, Interest_Rate):
	if(check_balance(account_amount, loan_amount,fees)):
		loan_period =loan_period + 1
		total_amount = total_amount+ loan_amount(1+Interest_Rate/600) + fees
		if (loan_period == 6):
			loan_status= "Completed"
			
if __name__ == "__main__":
    submit_loan(account_amount, loan_amount, Interest_Rate)

	
	
