<div class="card">
  <slot></slot>
</div>

<style>
  .card {
    border-radius: 15px;
    padding: 30px 30px;
    margin: 10px 10px;
    position: relative;
    border: 1px solid transparent;
    background:
      linear-gradient(45deg, #181825, #252538) padding-box padding-box,
      linear-gradient(to right, #cba6f77c, #89b4fa79) border-box;
  }

  .card:hover {
    border: 1px solid transparent;
    border-color: #cdd6f47a;
    background: linear-gradient(45deg, #1e1e2e, #cba6f720) border-box;
  }
</style>
