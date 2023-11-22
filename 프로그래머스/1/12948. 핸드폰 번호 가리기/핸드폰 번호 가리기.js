function solution(phone_number) {
    const hide = '*'.repeat(phone_number.length - 4);
    const show = phone_number.substring(phone_number.length - 4);
    return `${hide}${show}`;
}