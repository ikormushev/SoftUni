quota_minutes = int(input())
quota_sec = int(input())
length_m = float(input())
hundred_m_sec = int(input())

quota_total_sec = quota_minutes * 60 + quota_sec

slow_time_sec = (length_m / 120) * 2.5
skeleton_time_sec = (length_m / 100) * hundred_m_sec - slow_time_sec

if skeleton_time_sec <= quota_total_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {skeleton_time_sec:.3f}.")
else:
    time_diff = skeleton_time_sec - quota_total_sec
    print(f"No, Marin failed! He was {time_diff:.3f} second slower.")
