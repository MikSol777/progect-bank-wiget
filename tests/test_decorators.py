from src.decorators import log


@log()
def func_test(x, y):
    return x + y


def test_logs(capsys):
    func_test(1, 2)
    captured = capsys.readouterr()
    assert "func_test ok\n" == captured.out


def test_my_function(capsys):
    func_test(2, "2")
    captured = capsys.readouterr()
    assert captured.out == "func_test error: TypeError Inputs: (2, '2'), {}\n"


@log(filename="mylog.txt")
def func_test_1(x, y):
    return x + y


func_test_1(1, "2")
with open("mylog.txt", "r", encoding="utf-8") as file:
    content = file.read()
    assert content == "func_test_1 error: TypeError Inputs: (1, '2'), {}"


@log(filename="mylog.txt")
def func_test_2(x, y):
    return x + y


func_test_2(1, 2)
with open("mylog.txt", "r", encoding="utf-8") as file:
    content = file.read()
    assert content == "func_test_2 ok"
