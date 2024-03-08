

# 開發步驟

## 使用devcontainer的話
進入到虛擬機之後

### 切換到root
1.  su root

### 安裝poetry
2. curl -sSL https://install.python-poetry.org | python3 -

### 設定poetry變數
3. expot PATH="${PATH}:${HOME}/.local/bin" 

### 設定poetry 不要創建虛擬機
4. poetry config virtualenvs.create false

檢查設定是否成功
poetry config --list

### 安裝套件
5. poetry install

### 執行程式
5. python manage.py runserver


### 執行後進入admin頁面
創建school-admin的group，把管理者的帳號加上school-admin的group
