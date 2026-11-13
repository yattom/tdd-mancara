# worklog

やったこと、考えたこと、試行錯誤のメモ。新しいものを下に追記する。

## 2026-11-13

### 12:39〜 セッション開始

- 空のディレクトリから開始した。グローバルの CLAUDE.md をプロジェクトにコピーした。
- プロジェクト固有のことは CLAUDE.md ではなく README.md などに書く方針にした。
- README.md に演習の目的・概要と、お題「環のマンカラ」STEP 01 を転記し、最初のコミットをした。
- `.idea/` と `*.iml` は `~/.gitignore` で除外されている。IDE のファイルは ignore のままでよいことにした。

### 12:58 ブランチ戦略と記録の方針

- t-wada さんの記事（取得できたのは冒頭の約1/4）を確認した。`setup` や `step-01-1` のように作業ごとにブランチを切り、Stacked PR にしていた。コミットは TDD のステップごとに細かく、Red の状態もコミットしていた。
- やっとむの案は2つだった。develop を1本切ってずっとそこで進める案と、フィーチャーブランチを切って区切りで develop にマージする案。後者に決めた → [ADR 0001](adr/0001-branch-strategy.md)
- 決定の記録は略式 ADR と worklog に分けることにした → [ADR 0002](adr/0002-recording-decisions-and-worklog.md)
- この作業自体を `docs/working-rules` ブランチで行い、develop に `--no-ff` でマージした。
