# Leet Code Challenges: Practice

This repository contains solutions to [Leet Code](https://leetcode.com/) easy challenges. Each solution is organised by its corresponding problem number. Enter a specific keyword to search for a solution.

Search keyword: <input type="text" id="searchInput">

Click below to search for the string:

[Generate Greeting](javascript:void(0);)

<script>
document.querySelector('[href="javascript:void(0);"]').addEventListener('click', function() {
  const name = document.getElementById('searchInput').value;
  const searchUrl = `https://github.com/VasanthVanan/leet-code-challenges?search=${encodeURIComponent(name)}`;
  window.location.href = searchUrl;
});
</script>