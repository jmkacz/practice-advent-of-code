use std::collections::HashSet;

pub fn parse(lines: &Vec<&str>) -> Vec<i32> {
    let mut values: Vec<i32> = vec![0; lines.len()];
    for index in 0..lines.len() {
        values[index] = lines[index].parse().unwrap();
    }
    return values;
}

pub fn find_triple(values: &Vec<i32>, target: i32) -> [i32; 3] {
    let mut result = [0, 0, 0];
    let values: HashSet<_> = values.iter().cloned().collect();

    for first in &values {
        for second in &values {
            if first == second {
                continue;
            }
            let third = target - first - second;
            if values.contains(&third) && *first != third && *second != third {
                result = [*first, *second, third];
                result.sort();
                break;
            }
        }
    }

    return result;
}

pub fn compute_answer(lines: &Vec<&str>, target: i32) -> i32 {
    let values = parse(&lines);
    let results = find_triple(&values, target);
    return results[0] * results[1] * results[2];
}
