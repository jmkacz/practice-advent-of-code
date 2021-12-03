use std::collections::HashSet;

pub fn parse(lines: &Vec<&str>) -> Vec<i32> {
    let mut values: Vec<i32> = vec![0; lines.len()];
    for index in 0..lines.len() {
        values[index] = lines[index].parse().unwrap();
    }
    return values;
}

pub fn find_pair(values: &Vec<i32>, target: i32) -> [i32; 2] {
    let mut result: [i32; 2] = [0, 0];
    let values: HashSet<_> = values.iter().cloned().collect();

    for value in &values {
        if values.contains(&(target - value)) {
            result = [*value, target - value];
            result.sort();
            break;
        }
    }

    return result;
}

pub fn compute_answer(lines: &Vec<&str>, target: i32) -> i32 {
    let values = parse(&lines);
    let results = find_pair(&values, target);
    return results[0] * results[1];
}
