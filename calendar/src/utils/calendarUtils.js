export const fromTo = (a, b, includes = false) => {

  if (includes) {
    b.add(1, 'd');
  }

  let days = [];
  let current = a.clone();

  while (current.isBefore(b)) {
    days.push(current.clone());
    current.add(1, 'day');
  }
  return days;
};

export const month = (mnth) => {

  let daysBefore = [];
  let daysAfter = [];

  const _first = mnth.clone().startOf('month');
  const _last = mnth.clone().endOf('month');

  const monthDays = fromTo(_first, _last);

  // VISIBLE DAYS BEFORE FIRST OF MONTH
  if (_first.day() !== 1) {
    const _before = ((_first.day() + 6) % 7);

    daysBefore = fromTo(
      _first.clone().subtract(_before, 'days'),
      _first.clone()
    );
  }

  // VISIBLE DAYS AFTER LAST OF MONTH
  if (_last.day() !== 0) {
    const _after = (7 - _last.day());

    daysAfter = fromTo(
      _last.clone().add(1, 'days'),
      _last.clone().add(1 + _after, 'days')
    );
  }
  return daysBefore.concat(monthDays, daysAfter);
};