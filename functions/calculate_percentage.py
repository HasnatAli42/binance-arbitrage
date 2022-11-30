def calculate_percentages(initial: float, final: float):
    commission_usd = float(initial * 0.001) * 3
    gross_increase_USD = final - initial
    net_increase_USD = gross_increase_USD - commission_usd
    gross_increase_percent = float(final - initial)/initial*100
    net_increase_percent = gross_increase_percent - 0.3
    return gross_increase_USD, net_increase_USD, gross_increase_percent, net_increase_percent
