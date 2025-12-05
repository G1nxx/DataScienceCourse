def main():
    grades = [85, 92, 78, 90, 85, 88, 92, 78, 85, 90]
    res = {}
    max_val = grades[0]
    min_val = grades[0]
    sum_val = 0
    marks_map = {}
    
    for val in grades:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        sum_val += val
        
        if val in marks_map:
            marks_map[val] += 1
        else:
            marks_map[val] = 1
    
    average_val = sum_val // len(grades)
    
    res['average'] = average_val
    res['max'] = max_val
    res['min'] = min_val
    res['distribution'] = marks_map
    
    high_grades = []
    for key, count in marks_map.items():
        if key > 85:
            for _ in range(count):
                high_grades.append(key)
    
    res['high_grades'] = high_grades
    print(res)

if __name__ == '__main__':
    main()