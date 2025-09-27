// main.js - Front-end interactions for Job Application Tracker

$(function () {
  // ---------------------------------------------
  // Client-side validation (Bootstrap-style)
  // ---------------------------------------------
  const form = document.getElementById('applicationForm');
  if (form) {
    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  }

  // ---------------------------------------------
  // Filter by status on applications page
  // ---------------------------------------------
  const statusFilter = $('#statusFilter');
  const table = $('#applicationsTable');

  function updateSummary() {
    const rows = table.find('tbody tr');
    let total = 0, applied = 0, interview = 0, rejected = 0, offer = 0;
    rows.each(function () {
      const visible = $(this).is(':visible');
      if (!visible) return;
      total += 1;
      const s = ($(this).data('status') || '').toString().toLowerCase();
      if (s === 'applied') applied += 1;
      else if (s === 'interview') interview += 1;
      else if (s === 'rejected') rejected += 1;
      else if (s === 'offer') offer += 1;
    });
    $('#summary-total').text(`Total: ${total}`);
    $('#summary-applied').text(`Applied: ${applied}`);
    $('#summary-interview').text(`Interview: ${interview}`);
    $('#summary-rejected').text(`Rejected: ${rejected}`);
    $('#summary-offer').text(`Offer: ${offer}`);
  }

  function applyFilter() {
    const val = (statusFilter.val() || 'All').toString().toLowerCase();
    table.find('tbody tr').each(function () {
      const s = ($(this).data('status') || '').toString().toLowerCase();
      if (val === 'all' || s === val) $(this).show();
      else $(this).hide();
    });
    updateSummary();
  }

  if (statusFilter.length && table.length) {
    statusFilter.on('change', applyFilter);
    applyFilter(); // initialize on page load
  }

  // ---------------------------------------------
  // Delete confirmation modal
  // ---------------------------------------------
  const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'), {});
  const delCompany = document.getElementById('delCompany');
  const deleteForm = document.getElementById('deleteForm');

  $(document).on('click', '.btn-delete', function () {
    const id = $(this).data('id');
    const company = $(this).data('company');
    if (delCompany) delCompany.textContent = company || 'this company';
    if (deleteForm) deleteForm.action = `/delete/${id}`;
    if (deleteModal) deleteModal.show();
  });
});
