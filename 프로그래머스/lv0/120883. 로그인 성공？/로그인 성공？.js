function solution(id_pw, db) {
    const [id, pw] = id_pw;
    for (item of db) {
        const [targetId, targetPw] = item;
        if (id === targetId && pw === targetPw) return "login";
        if (id === targetId) return "wrong pw";
    }
    return "fail";
}