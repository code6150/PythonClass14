import db

# 데이터베이스 테이블 생성

# 관계형 데이터 베이스 ( mariadb, mysql ... )
#   - 외래키 사용 ( foreign key ) -> 다른 테이블에 있는 값과 연결을 지을 수 있음.
#   - primary key ( 해당 테이블에서 컬럼을 찾는 정보로서, unique[1개만 존재] 함. )

db.execute("create table if not exists `info` (`id` char(8) primary key not null, `pw` text not null, `nick` text not null)")

# 회원 정보를 담는 클래스
# id, nick
class User:
    def __init__(self, id, nickname):
        self.id = id
        self.nickname = nickname


# 1. 메뉴 출력
#   - 회원가입/로그인 선택 ( 1, 2 번 아닌경우 메세지 출력 )
#   - 1. 로그인
#   - 2. 회원가입
#   - 입력 >>


# 2. 로그인
#   - 사용자에게 아이디/비번 입력받음
#   - 해당 데이터가 데이터 베이스에 존재하는지 여부 확인
#   - 존재하면 로그인 성공 / 존재하지 않으면 로그인 실패
#   - 회원 정보를 담는 클래스를 반환

def login():
    id = input("id를 입력해주세요 >>> ")
    password = input("password를 입력해주세요 >>> ")
    db.execute(f"select * from `info` where `id` = '{id}' and `pw` = '{password}'")
    data = db.fetchall() # ((0-id, 1-pw, 2-nick))
    if len(data) == 0:
        print('아이디나 비번이 잘못 되었습니다.')
        return None;
    else:
        return User(data[0][0], data[0][2])


# 3. 회원가입
#   - 사용자에게 아이디/비번/닉네임 입력받음
#   - 해당 데이터가 데이터 베이스에 존재하는지 여부 확인
#   - 존재하면 회원가입 실패 / 존재하지 않으면 회원가입 성공

def sign_in():
    id = input('아이디를 입력해 >>> ')
    password = input('비번도 입력해 >>> ')
    nick = input('닉넴도 >>> ')
    db.execute(f"select * from `info` where `id` = '{id}'")
    if len(db.fetchall()) == 0:
        #일치하는 데이터가 없다 ( 가입가능 )
        db.execute(f"insert into `info` (`id`,`pw`,`nick`) values('{id}','{password}','{nick}')")
        db.commit()
        return True
    else:
        # 일치하는 데이터가 있다 ( 가입 불가 )
        print('이미 존재하는 아이디입니다.')
        return False

def get_user():
    while True:
        print("=" * 30)
        print("1.로그인")
        print("2.회원가입")
        print("=" * 30)
        try:
            answer = int(input('입력 >>> '))
        except:
            print("-_-")
            continue

        if answer == 1:
            user = login()
            if user:
                return user
        elif answer == 2:
            sign_in()
        else:
            print('잘못된 입력입니다.')

get_user()