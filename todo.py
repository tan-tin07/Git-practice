# todo.py
# 할 일 관리 프로그램
#
# 안내:
#   1. 이 파일의 이름을 todo.py로 변경하세요.
#   2. TODO 주석을 읽고 각 함수를 완성하세요.
#   3. if __name__ 블록의 테스트 코드는 수정하지 마세요.

# 할 일 목록을 저장하는 리스트
# 각 항목은 딕셔너리 형태: {"task": "할 일 내용", "done": False}
todo_list = []


def add_todo(task):
    """할 일 항목을 추가한다.

    Args:
        task (str): 추가할 할 일 내용

    Example:
        add_todo("파이썬 공부하기")
        → todo_list에 {"task": "파이썬 공부하기", "done": False} 추가
        → '파이썬 공부하기'이(가) 추가되었습니다. 출력
    """
    new_todo = {"task": task, "done": False}
    todo_list.append(new_todo)
    print(f"'{task}'이(가) 추가되었습니다.")
    # TODO: todo_list에 새 항목을 딕셔너리로 추가하세요
    # TODO: 추가 완료 메시지를 출력하세요
    pass


def show_todos():
    """전체 할 일 목록을 번호와 함께 출력한다.
    완료된 항목은 [✓], 미완료는 [ ]로 표시한다.
    목록이 비어있으면 안내 메시지를 출력한다.

    출력 예시:
        ==============================
               할 일 목록
        ==============================
          1. [ ] 파이썬 과제 완료하기
          2. [✓] Git 실습 지시서 읽기
        ==============================
    """
    if not todo_list:
        print("할 일이 없습니다.")
        return

    print("\n" + "=" * 30)
    print("       할 일 목록")
    print("=" * 30)

    for i, item in enumerate(todo_list, 1):
        # TODO: 완료 여부에 따라 status를 "✓" 또는 " "로 설정하세요
        # TODO: 번호, status, 할 일 내용을 형식에 맞게 출력하세요
        if item["done"]:
            status = "✓"
        else:
            status = " "
        print(f"  {i}. [{status}] {item['task']}")
        pass

    print("=" * 30)


def complete_todo(index):
    """지정한 번호의 할 일을 완료 처리한다.

    Args:
        index (int): 완료 처리할 항목 번호 (1부터 시작)

    Note:
        올바르지 않은 번호가 입력되면 안내 메시지를 출력하고 종료한다.
        힌트: 사용자에게 보여주는 번호는 1부터 시작하지만
              리스트 인덱스는 0부터 시작합니다.
    """
    # TODO: index가 유효한 범위인지 확인하고
    #       범위를 벗어나면 안내 메시지 출력 후 return하세요
    if index < 1 or index > len(todo_list):
        print("올바르지 않은 번호입니다.")
        return

    # TODO: 해당 항목의 "done" 값을 True로 변경하세요
    todo_list[index - 1]["done"] = True

    # TODO: 완료 메시지를 출력하세요
    print(f"'{todo_list[index - 1]['task']}' 항목이 완료 처리되었습니다.")
    pass


def count_todos():
    """전체 항목 수와 완료된 항목 수를 반환한다.

    Returns:
        tuple: (전체 수, 완료 수)

    Example:
        total, done = count_todos()
        print(f"전체 {total}개 중 {done}개 완료")
    """
    total = len(todo_list)
    # TODO: 완료된 항목 수를 계산하세요
    #       힌트: item["done"]이 True인 항목의 수를 세어보세요
    done = 0
    return total, done


if __name__ == "__main__":
    # 아래 테스트 코드를 실행하여 각 함수가 올바르게 동작하는지 확인하세요
    # 이 블록은 수정하지 마세요

    add_todo("파이썬 과제 완료하기")
    add_todo("Git 실습 지시서 읽기")
    add_todo("README.md 작성하기")
    show_todos()

    complete_todo(1)
    show_todos()

    total, done = count_todos()
    print(f"\n전체 {total}개 중 {done}개 완료")
