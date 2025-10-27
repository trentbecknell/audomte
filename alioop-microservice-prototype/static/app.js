// Format phone number to E.164 format
function formatPhoneNumber(phone) {
  if (!phone) return phone;
  
  // Remove all non-digit characters
  const digitsOnly = phone.replace(/\D/g, '');
  
  // If it starts with 1 and has 11 digits, it's already a US number with country code
  if (digitsOnly.length === 11 && digitsOnly.startsWith('1')) {
    return '+' + digitsOnly;
  }
  
  // If it has 10 digits, assume US and add country code
  if (digitsOnly.length === 10) {
    return '+1' + digitsOnly;
  }
  
  // If it has more than 10 digits, assume it includes country code
  if (digitsOnly.length > 10) {
    return '+' + digitsOnly;
  }
  
  // Otherwise return with + and hope for the best
  return '+' + digitsOnly;
}

async function createClient(e){
  e.preventDefault();
  const fd = new FormData(e.target);
  const payload = Object.fromEntries(fd.entries());
  if (!payload.delivery_custom_url) delete payload.delivery_custom_url;
  if (!payload.payment_custom_url) delete payload.payment_custom_url;
  
  // Format phone number automatically
  if (payload.phone) {
    const originalPhone = payload.phone;
    payload.phone = formatPhoneNumber(payload.phone);
    console.log(`Phone formatted: ${originalPhone} → ${payload.phone}`);
  }
  
  // Convert checkbox to boolean
  payload.use_masked_phone = payload.use_masked_phone === 'on';
  const resp = await fetch('/clients',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
  const data = await resp.json();
  if (data.masked_phone) {
    alert(`Client created with masked phone: ${data.masked_phone}`);
  }
  location.reload();
}
async function createProject(e){
  e.preventDefault();
  const fd = new FormData(e.target);
  const payload = Object.fromEntries(fd.entries());
  payload.client_id = parseInt(payload.client_id);
  if (!payload.client_id) {
    alert('Please select a client first.');
    return false;
  }
  await fetch('/projects',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
  location.reload();
}
function openSendToClient(clientId){
  document.getElementById('send_client_id').value = clientId;
  document.getElementById('sendDialog').showModal();
}
function openSend(projectId){
  const clientSelect = document.getElementById('clientSelect');
  document.getElementById('send_client_id').value = clientSelect.value;
  document.getElementById('sendDialog').showModal();
}
async function sendMessage(e){
  e.preventDefault();
  const fd = new FormData(e.target);
  const payload = Object.fromEntries(fd.entries());
  payload.client_id = parseInt(payload.client_id);
  await fetch('/send',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
  document.getElementById('sendDialog').close();
  alert('Message sent! Check server logs or your phone/email.');
}
async function completeProject(id){
  await fetch(`/projects/${id}/complete`,{method:'POST'});
  alert('Project marked complete; client notified based on preferences.');
  location.reload();
}
function toggleDeliveryCustom(val){
  document.getElementById('delivery_custom').style.display = (val==='Custom')?'block':'none';
}
function togglePaymentCustom(val){
  document.getElementById('payment_custom').style.display = (val==='Custom')?'block':'none';
}
