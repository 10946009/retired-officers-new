# 退除役官兵系統
用來給予退伍後的官兵報名用的系統
首頁:https://study.ntub.edu.tw/veteran

## 安裝步驟
透過docker安裝

docker build -t retired .
docker run -idt --name retired0330 -v "$(pwd):/app" -p 8000:8000  retired

## 使用說明
有分為使用者和管理者：
### 使用者
    - 使用者可以註冊>登入>報名活動
    - 報名後才可以列印報名表
    - 成績公布後可查看成績單
### 管理者
    - 管理者可以增刪改查活動&報名者
    - 資料審查功能可以登記報名者的報名狀態
    - 有報名編號後，可以輸入成績

    
