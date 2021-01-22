const bestSum = (targetSum, nums) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = []

    for (let i = 0; i <= targetSum; i++) {
        if (table[i] !== null) {
            for (let num of numbers) {
                const combination = [ ...table[i], num];
                if (!table[i + num] || table[i + num].length > combination.length) {
                    table[i + num] = combination;
                }
            }
        }
    }

    return table[targetSum];
}
