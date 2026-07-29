fn abs(num: f32) -> f32 {
    if num < 0.0 {
        return -1.0 * num;
    }

    num
}
#[test]
fn abs_tes() {
    assert_eq!(abs(-0.5), 0.5)
}

fn factorial(num: i128) -> i128 {
    let mut fact = 1i128;

    for i in 1..(num + 1) {
        fact *= i
    }

    return fact;
}

#[test]
fn factorial_test() {
    assert_eq!(factorial(5), 120);
    assert_eq!(factorial(0), 1)
}

// === exp ===
fn exp(x: f32, m: i32) -> f32 {
    let (mut e, mut e_ant) = (1.0, 0.0);

    let mut i = 1;
    while abs(e - e_ant) > 10f32.powi(-m) {
        e_ant = e;
        e += x.powi(i) / (factorial(i as i128) as f32);

        if i > 1000 {
            return e;
        }

        i += 1;
    }

    return e;
}

#[test]
fn exp_test() {
    assert_eq!(exp(1f32, 16), 2.718282)
}

fn main() {
    println!("{}", exp(5.0, 8))
}
