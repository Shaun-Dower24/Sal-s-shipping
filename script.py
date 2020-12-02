premium_ground_shipping = 125.00

def ground_shipping(weight):

  if weight <= 2.0:
    price_per_pound = 1.5

  elif weight <= 6.0:
    price_per_pound = 3.0

  elif weight <= 10.0:
    price_per_pound = 4.0

  else:
    price_per_pound = 4.75

  return 20 + (weight * price_per_pound)

def drone_shipping(weight):

  if weight <= 2.0:
    price_per_pound = 4.5

  elif weight <= 6.0:
    price_per_pound = 9.0

  elif weight <= 10.0:
    price_per_pound = 12.0

  else:
    price_per_pound = 14.25

  return weight * price_per_pound

def cheapest_shipping(weight):

  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping

  if ground < drone and ground < premium:
      method = "Standard ground"
      cost = ground
  elif drone < ground and drone < premium:
      method = "Standard drone"
      cost = drone
  else:
      method = "Premium"
      cost = premium
  print(

    "The cheapest shipping method is $%.2f with %s shipping."  % (cost, method)
    )

print(ground_shipping(8.4))
print(drone_shipping(1.5))
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))