class CashRegister:

  def __init__(self):
    self._itemcount = 0
    self._totalprice = 0.00

  def additems(self, price) :
    self._itemcount += 1
    self._totalprice = self._totalprice + price

  def gettotal(self):
    return self._totalprice

  def getcount(self):
    return self._itemcount

  def clear(self):
    self._itemcount = 0
    self._totalprice = 0.00

trans1 = CashRegister()
trans1.additems(10)
trans1.additems(3.99)
trans1.additems(19.99)
print(f'{trans1.getcount()} items')
print("%.2f" % trans1.gettotal())