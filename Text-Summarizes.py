# পূর্বের শব্দগুলি
previous_words = ['জ্বর', 'মাথাব্যাথা', 'সর্দি', 'কাশি', 'চোখে ব্যাথা', 'পায়ে ব্যাথা', 'গলা ব্যাথা', 'পেটে ব্যাথা', 'ক্ষুধা', 'গ্যাস', 'বুকে ব্যাথা']

# বাংলা বাক্য ইনপুট
bangla_sentence = input("বাংলা বাক্য লিখুন: ")

# বাক্য থেকে পূর্বের শব্দগুলি বের করা
matching_words = [word for word in previous_words if word in bangla_sentence]

# পূর্বের শব্দগুলি যে শব্দগুলির সাথে মিলেছে তাদের প্রিন্ট করা
print("পূর্বের শব্দগুলি যে শব্দগুলির সাথে মিলেছে:", matching_words)
