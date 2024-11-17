# tester.py

from geo.utils import add, subtract  # geo 패키지에서 함수 가져오기

def test_add():
    assert add(3, 2) == 5  # 3 + 2 = 5가 맞는지 테스트
    print("add() 테스트 성공!")

def test_subtract():
    assert subtract(5, 3) == 2  # 5 - 3 = 2가 맞는지 테스트
    print("subtract() 테스트 성공!")

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("모든 테스트 통과!")
