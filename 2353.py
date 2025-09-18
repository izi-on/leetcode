from collections import defaultdict
import heapq


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.category_to_heap = defaultdict(list)
        self.food = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.track_latest_rating = {}
        self.food_to_category = {}
        for i in range(len(foods)):
            self.food_to_category[foods[i]] = cuisines[i]
        for i, f in enumerate(foods):
            self.changeRating(f, ratings[i])

    def changeRating(self, food: str, newRating: int) -> None:
        food_category = self.food_to_category[food]
        print("rating", self.category_to_heap[food_category], (-newRating, food))
        heapq.heappush(self.category_to_heap[food_category], (-newRating, food))
        self.track_latest_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        print("highest")
        print(cuisine)
        heap = self.category_to_heap[cuisine]
        print(heap)
        while heap and -heap[0][0] != self.track_latest_rating[heap[0][1]]:
            heapq.heappop(heap)
            print("popped", heap)
        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
