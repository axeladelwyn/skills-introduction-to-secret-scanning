def add_expense(expenses, amount, category):
        expenses.append({'amount': amount, 'category': category})
def print_expenses(expenses):
        for expense in expenses:
            print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
def total_expenses(expenses):
       return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
        lambda expense: expense['category'] == category
        return filter(lambda expense: expense['category'] == category, expenses)
def main():
        expenses = [1, 2, 3]
        while True:
                print('\nExpense Tracker')
                print('1. Add Expense')
                print('2. Print Expenses')
                print('3. Total Expenses')
                print('4. Filter by Category')
                print('5. Exit')
                choice = input('Enter your choice: ')
                if choice == '1':
                        amount = float(input('Enter amount: '))
                        category = input('Enter category: ')
                        add_expense(expenses, amount, category)
                elif choice == '2':
                        print('\nAll Expenses')
                        print_expenses(expenses)
                elif choice == '3':
                        print(f'Total Expenses: {total_expenses(expenses)}')
                elif choice == '4':
                        category = input('Enter category: ')
                        print(f'{category} Expenses')
                        print_expenses(filter_expenses_by_category(expenses, category))
                elif choice == '5':
                        print('Exiting...')
                        break
if __name__ == '__main__':
        main()
        