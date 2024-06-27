using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace ashuwebApp.Pages.Account
{
    public class LoginModel : PageModel
    {
        [BindProperty]
        public string Username { get; set; }
        
        [BindProperty]
        public string Password { get; set; }

        public void OnGet()
        {
        }

        public IActionResult OnPost()
        {
            // For now, just redirect to the home page
            // You can add logic to validate the user credentials here
            if (Username == "admin" && Password == "password")
            {
                // Normally, you would set up authentication here
                return RedirectToPage("/Index");
            }

            // If login fails, redisplay the form with an error message
            ModelState.AddModelError(string.Empty, "Invalid login attempt.");
            return Page();
        }
    }
}

