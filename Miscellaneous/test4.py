from collections import defaultdict


class RewardPoints:
    def __init__(self):
        self.customers = defaultdict(int)

    def earn_points(self, customer_name, points):
        if customer_name not in self.customers:
            self.customers[customer_name] += 500

        if points > 0:
            self.customers[customer_name] += points

    def spend_points(self, customer_name, points):
        if customer_name not in self.customers:
            return 0
        elif points <= 0:
            return self.customers[customer_name]
        elif self.customers[customer_name] >= points:
            self.customers[customer_name] -= points
        return self.customers[customer_name]


rewardPoints = RewardPoints()
rewardPoints.earn_points('John', 520)
rewardPoints.earn_points('John', 0)
print(rewardPoints.spend_points('John', 20))
print(rewardPoints.spend_points('John', 100))
print(rewardPoints.spend_points('mary', 200))
print(rewardPoints.spend_points('mary', 0))
