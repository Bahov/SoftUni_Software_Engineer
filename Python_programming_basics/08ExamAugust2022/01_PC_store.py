processor_price = float(input())
video_card_price = float(input())
ram_price = float(input())
number_ram_cards = int(input())
discount_perc = float(input())

video_processor_price_usd = processor_price + video_card_price

video_processor_usd_with_discount = video_processor_price_usd * (1 - discount_perc)

ram_card_price_usd = ram_price * number_ram_cards

total_price_bgn_with_discount = (video_processor_usd_with_discount + ram_card_price_usd) * 1.57

print(f"Money needed - {total_price_bgn_with_discount:.2f} leva.")