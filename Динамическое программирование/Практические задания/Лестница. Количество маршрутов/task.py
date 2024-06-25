from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени
    if not isinstance(count_stairs,int):
        raise (TypeError)
    if count_stairs<0:
        raise(ValueError)
    if count_stairs==0:
        return [0]
    if count_stairs==1:
        return [0,1]
    # stair_prev,stair_finish=1,1
    # result_list = [1, 1]
    #
    # for _ in range (2,count_stairs+1):
    #     stair_prev,stair_finish=stair_finish, stair_finish+stair_prev
    #     result_list.append(stair_finish)
    # return result_list
    result_list=[0 for _ in range (count_stairs+1)]
    result_list[0],result_list[1]=0,1
    for i in range (2,count_stairs+1):
        result_list[i]=result_list[i-1]+result_list[i-2]
    return result_list
if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
