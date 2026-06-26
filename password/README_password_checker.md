# Password Checker / Complexity Tool (`password/password_checker.py`)

## What it does
Evaluates password strength based on simple criteria and prints a strength label.

### Criteria (5 checks)
- Length >= 8
- At least one uppercase letter `A-Z`
- At least one lowercase letter `a-z`
- At least one digit `0-9`
- At least one special character matching `\W` or `_`

## File
- `password/password_checker.py`

## Run
```bash
python password/password_checker.py
```

## How to use
- Enter a password to check
- Type `exit` to stop

## Output
The script prints:
- A checkbox-style report for each criterion
- A final strength category:
  - VERY STRONG
  - STRONG
  - MEDIUM
  - WEAK

