import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email(sender_email, receiver_email, subject, body, app_password):
    # SMTP 서버 설정
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # 이메일 헤더 및 본문 설정 (UTF-8 인코딩)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    # 제목을 UTF-8로 인코딩
    msg['Subject'] = Header(subject, 'utf-8')

    # 이메일 본문 추가 (UTF-8 인코딩)
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        # Gmail 서버에 연결 및 로그인
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS(보안 연결) 시작
        server.login(sender_email, app_password)

        # 이메일 전송
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("이메일이 성공적으로 전송되었습니다!")

    except Exception as e:
        print(f"이메일 전송 중 오류가 발생했습니다: {e}")

    finally:
        server.quit()

# 사용 예시
sender_email = "wwwe7701@gmail.com"  #보낼 이메일
receiver_email = "24s620h0659@sonline20.sen.go.kr" # 받을 이메일
subject = "제설작업 시작"  # 한글 제목
body = "눈이 탐지 되어 제설 작업을 시작합니다. "  # 한글 본문
app_password = "//////"  # 구글 계정에서 생성한 앱 비밀번호 입력 (2차 인증)

send_email(sender_email, receiver_email, subject, body, app_password)
