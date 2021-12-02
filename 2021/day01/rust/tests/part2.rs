use advent::part2::*;

use std::str::FromStr;

#[test]
fn test_parse() {
    let lines = vec![
        "199", "200", "208", "210", "200", "207", "240", "269", "260", "263",
    ];
    let actual = parse(&lines);
    let expected = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    assert_eq!(actual, expected);
}

#[test]
fn test_compute_answer_sample() {
    let lines = vec![
        "199", "200", "208", "210", "200", "207", "240", "269", "260", "263",
    ];
    let actual = compute_answer(&lines);
    let expected: i32 = 5;
    assert_eq!(actual, expected);
}

// Borrowed from: https://dev.to/dandyvica/different-ways-of-reading-files-in-rust-2n30
// Borrowed from: https://stackoverflow.com/questions/36020110/how-do-i-avoid-unwrap-when-converting-a-vector-of-options-or-results-to-only-the
fn get_lines<T: FromStr>(filename: &str) -> Vec<T> {
    std::fs::read_to_string(filename)
        .expect("file not found!")
        .lines()
        .map(|x| x.parse())
        .collect::<Vec<Result<T, <T as FromStr>::Err>>>()
        .into_iter()
        .filter_map(|e| e.ok())
        .collect()
}

#[test]
fn test_compute_answer_full() {
    let lines = get_lines::<String>("../data/input.dat");
    // Vec<String> => Vec<&str>
    let lines: Vec<&str> = lines.iter().map(|x| x.as_ref()).collect();
    let actual = compute_answer(&lines);
    let expected: i32 = 1734;
    assert_eq!(actual, expected);
}
