import Login
import db
import os
import openai

openai.api_key = os.getenv("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")

my_prompt = "You: What have you been up to?\nFriend: Watching old movies.\nYou: What's the name of the movie?\nFriend:"

def get_message(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.5,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    return response.choices[0].text

# __name__ -> 만약 이 파일이 실행 된 파일 인 경우
#       값 = __main_-

# __name__ -> 만약 이 파일이 실행된 파일의 import 된 파일인 경우
#       값 - 파일 이름
# 배우기 ~> user: ~~~? q: ~~~? a: ~~~?
db.execute("create table if not exists `message` (`user_id` char(8) not null, `q` text not null, `a` text not null, foreign key (`user_id`) references `info` (`id`) on delete cascade)")

def generate_message():
    global my_prompt
    db.execute("select * from `message`")
    data = db.fetchall()
    for tu in data:
        my_prompt += "\nYou: " + tu[1] + "\nFriend: " + tu[2]
if __name__ == '__main__':
    user = Login.get_user()
    print(f'chatbot: {user.nickname}님 ㅎㅇ')
    while True:
        text = input('나 : ')
        if text == "배우기":
            q = input('Q : ')
            a = input('A : ')
            db.execute(f"insert into `message` (`user_id`, `q`, `a`) values('{user.id}','{q}','{a}')")
            db.commit()
        else:
            generate_message()
            my_prompt += "\nYou: " + text + "\nFriend: "
            print(f"chatbot :  {get_message(my_prompt)}")