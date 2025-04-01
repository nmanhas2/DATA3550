from decimal import Decimal

class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""

    def __init__(self, first_name, last_name,gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self.gross_sales = gross_sales  # validate via property
        self.commission_rate = commission_rate  # validate via property

    def first_name(self):
        return self._first_name

    def last_name(self):
        return self._last_name

    def gross_sales(self):
        return self._gross_sales

    def gross_sales(self, sales):

        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self._gross_sales = sales

    def commission_rate(self):
        return self._commission_rate


    def commission_rate(self, rate):

        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
               'Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earnings(self):

        return self.gross_sales * self.commission_rate

    def __repr__(self):

        return (f'gross sales: {self.gross_sales:.2f}\n' +
            f'commission rate: {self.commission_rate:.2f}')

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets paid a salary plus
    commission based on gross sales."""

    def __init__(self, first_name, last_name, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, gross_sales, commission_rate)
        self.base_salary = base_salary  # validate via property

    def base_salary(self):
        return self._base_salary

    def base_salary(self, salary):
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be >= to 0')

        self._base_salary = salary

    def earnings(self):
        return super().earnings() + self.base_salary

    def __repr__(self):
        return ('Salaried' + super().__repr__() +
            f'\nbase salary: {self.base_salary:.2f}')