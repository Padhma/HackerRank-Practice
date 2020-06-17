#  A median on the hypotenuse divides the right angled triangle into two isoceles triangle. Means AM=BM=CM. So, ∡MBC = ∡MCB
import math
AB = int(input())
BC = int(input())

print( round(math.degrees(math.atan2(AB,BC))), chr(176), sep="" )