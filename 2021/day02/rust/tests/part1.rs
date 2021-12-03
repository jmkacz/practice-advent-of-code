use advent::part1::*;

use std::str::FromStr;

#[test]
fn test_compute_answer_sample() {
    let lines = vec![
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ];
    let actual = compute_answer(&lines);
    let expected: i32 = 150;
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
    let expected: i32 = 1480518;
    assert_eq!(actual, expected);
}
