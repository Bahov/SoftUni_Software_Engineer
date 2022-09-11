packet_weight = float(input())
service_type = input()
distance_km = int(input())

final_price_st = 0
additional = 0
if service_type == "standard":
    if packet_weight < 1:
        final_price_st = distance_km * 3
    elif packet_weight < 10:
        final_price_st = distance_km * 5
    elif packet_weight < 40:
        final_price_st = distance_km * 10
    elif packet_weight < 90:
        final_price_st = distance_km * 15
    elif packet_weight < 150:
        final_price_st = distance_km * 20
elif service_type == "express":
    if packet_weight < 1:
        final_price_st = distance_km * 3
        additional = (3 * 0.8 * packet_weight * distance_km)
    elif packet_weight < 10:
        final_price_st = distance_km * 5
        additional = (5 * 0.4 * packet_weight * distance_km)
    elif packet_weight < 40:
        final_price_st = distance_km * 10
        additional = (10 * 0.05 * packet_weight * distance_km)
    elif packet_weight < 90:
        final_price_st = distance_km * 15
        additional = (15 * 0.02 * packet_weight * distance_km)
    elif packet_weight < 150:
        final_price_st = distance_km * 20
        additional = (20 * 0.01 * packet_weight * distance_km)

final_price_leva = (final_price_st + additional) / 100

print(f"The delivery of your shipment with weight of {packet_weight:.3f} kg. would cost {final_price_leva:.2f} lv.")
