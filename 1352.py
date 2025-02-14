class ProductOfNumbers:
    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(num * self.prefix_prod[-1])

    def getProduct(self, k: int) -> int:
        prod_len = len(self.prefix_prod) - 1
        if k > prod_len:
            return 0
        else:
            return self.prefix_prod[-1] // self.prefix_prod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
