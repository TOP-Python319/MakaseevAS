def numbers_strip(numbers_list: list[float], n: int=1, copy: bool=False) -> list[float]:
    if copy:       
        return numbers_list.copy()
    else :
        for _ in range(n):
            numbers_list.remove(min(numbers_list)) #удаление минимального числа
            numbers_list.remove(max(numbers_list)) #удаление максимального числа
        return numbers_list
    
sample = [1, 2, 3, 4]
sample_stripped = numbers_strip(sample)
print(sample_stripped)

sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)

#[2, 3]
#[10, 20, 30, 40, 50]