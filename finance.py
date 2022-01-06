test = 1


def quick_ratio(cash_equivalents, marketable_securities, accounts_receivables, current_liabilities):
    return (int(cash_equivalents) + int(marketable_securities) + int(accounts_receivables))/int(current_liabilities)


def current_ratio(current_assets, current_liabilities):
    return (int(current_assets))/int(current_liabilities)


def cash_ratio(cash_and_cash_equivalents, current_liabilities):
    return (int(cash_and_cash_equivalents))/int(current_liabilities)


def operating_cash_flow_ratio(operating_cash_flow, current_liabilities):
    return (int(operating_cash_flow))/int(current_liabilities)


def receivables_turnover_ratio(credit_sales):
    a1 = input("What is your accounts receivable at the begining of the year? ")
    a2 = input("What is your accounts receivable at the end of the year? ")
    acr = (int(a1) + int(a2))/2
    return (int(credit_sales))/int(acr)


def main():
    cash_equivalents = input("What are your cash equivalents? ")
    marketable_securities = input("What are your marketable securities? ")
    accounts_receivables = input("What are your accounts receivable? ")
    current_liabilities = input("What are your current liabilities? ")
    current_assets = input("What are your current assets? ")
    operating_cash_flow = input("What is your operating cash flow? ")
    cash_and_cash_equivalents = input(
        "What are your cash and cash equivalents? ")
    credit_sales = input("What are your credit sales? ")

    qr = quick_ratio(cash_equivalents, marketable_securities,
                     accounts_receivables, current_liabilities)
    cr = current_ratio(current_assets, current_liabilities)
    cash_r = cash_ratio(cash_and_cash_equivalents, current_liabilities)
    op_cash_fl = operating_cash_flow_ratio(
        operating_cash_flow, current_liabilities)
    rec_tr = receivables_turnover_ratio(credit_sales)

    print(qr)
    print(cr)
    print(cash_r)
    print(op_cash_fl)
    print(rec_tr)


main()
