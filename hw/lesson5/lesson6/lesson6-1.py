from edu.tools import calculate_bmi as a
from edu.tools import get_state as b

def main():
    # BMI計算171
    try:
        height:int = int(input('請輸入你的身高(公分 cm):'))        
        weight = eval(input('請輸入你的體重(公斤 kg):'))        
        bmi =edu.tools.calculate_bmi(height,weight)
    except ValueError:
        print('輸入發生錯誤')
    except Exception as e :
        print(e)
    else:
        print(f'你的身高:{height} 公分')
        print(f'你的體重:{weight:.2f} 公斤')
        print(f'你的 BMI值為:{bmi:.2f}')
        print(edu.tools.get_state(bmi))

if __name__ == "__main__":
    main()