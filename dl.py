import sys, os
from skillshare import Skillshare, splash

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = "device_session_id=3d45f68b-bf7b-4963-a41e-e7ef75bff9cb; show-like-copy=0; YII_CSRF_TOKEN=eFJMTTRzWHUwVGRRWkZ6bVgyMXlvVGVDenhSa1NPR3mg0_m4turhakLIsQWZ-XsuarjFtdQWoUer4caj9wKOyQ%3D%3D; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; __stripe_mid=13d8b4ee-7f81-4653-a499-80fb2918c36a8d6f2a; CAPTIONS=off; __stripe_sid=e7614d30-86c7-41e7-8c3f-5f2d9e0c3f896938c1; ss_hide_default_banner=1607554837.697; __cf_bm=c7fe0169edac98758a4ae4a07ff516acb4653070-1607554839-1800-Ae/MlTLZnugVGcm6c17UVS+26Wh7VSJ0C1Tif03J+IQi6d/noWmScvBHBQrEJcNGAfPT6gcruOs/2a/v3Aqn8qY7vUE4FqFNhymLyiv3ZyPE4BHnQeBgz8uSilrwl9eCLg==; PHPSESSID=a57c738cf5d38833648f96549b66fbc7; skillshare_user_=7a6cec0461cf9fbcf93c1feedc49869de0b623fca%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2216802844%22%3Bi%3A1%3Bs%3A28%3A%22skill0303%40temporary-mail.net%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22297029121%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222020-12-09%2023%3A01%3A38%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222020-12-09%2023%3A02%3A34%22%3B%7D%7D"
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
